import asyncio
import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun
import os
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from typing import Optional

@function_tool()
async def get_weather(
    context: RunContext,  # type: ignore
    city: str) -> str:
    """
    Get the current weather for a given city.
    """
    loop = asyncio.get_event_loop()
    try:
        response = await loop.run_in_executor(
            None, 
            lambda: requests.get(f"https://wttr.in/{city}?format=3")
        )
        if response.status_code == 200:
            logging.info(f"Weather for {city}: {response.text.strip()}")
            return response.text.strip()   
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"Could not retrieve weather for {city}."
    except Exception as e:
        logging.error(f"Error retrieving weather for {city}: {e}")
        return f"An error occurred while retrieving weather for {city}." 

@function_tool()
async def search_web(
    context: RunContext,  # type: ignore
    query: str) -> str:
    """
    Search the web using DuckDuckGo.
    """
    loop = asyncio.get_event_loop()
    try:
        results = await loop.run_in_executor(
            None,
            lambda: DuckDuckGoSearchRun().run(tool_input=query)
        )
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."    

@function_tool()    
async def send_email(
    context: RunContext,  # type: ignore
    to_email: str,
    subject: str,
    message: str,
    cc_email: Optional[str] = None
) -> str:
    """
    Send an email through Gmail.
    
    Args:
        to_email: Recipient email address
        subject: Email subject line
        message: Email body content
        cc_email: Optional CC email address
    """
    loop = asyncio.get_event_loop()
    try:
        await loop.run_in_executor(
            None,
            lambda: _send_email_sync(to_email, subject, message, cc_email)
        )
        logging.info(f"Email sent successfully to {to_email}")
        return f"Email sent successfully to {to_email}"
        
    except smtplib.SMTPAuthenticationError:
        logging.error("Gmail authentication failed")
        return "Email sending failed: Authentication error. Please check your Gmail credentials."
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
        return f"Email sending failed: SMTP error - {str(e)}"
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        return f"An error occurred while sending email: {str(e)}"

def _send_email_sync(to_email, subject, message, cc_email):
    # Gmail SMTP configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Get credentials from environment variables
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")  # Use App Password, not regular password
    
    if not gmail_user or not gmail_password:
        raise ValueError("Gmail credentials not found in environment variables")
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Add CC if provided
    recipients = [to_email]
    if cc_email:
        msg['Cc'] = cc_email
        recipients.append(cc_email)
    
    # Attach message body
    msg.attach(MIMEText(message, 'plain'))
    
    # Connect to Gmail SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption
    server.login(gmail_user, gmail_password)
    
    # Send email
    text = msg.as_string()
    server.sendmail(gmail_user, recipients, text)
    server.quit()