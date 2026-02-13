import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime


def send_engagement_notification(session_id: str, first_message: str, user_email: str = None):
    """
    Send email notification when someone engages with the digital twin

    Args:
        session_id: The conversation session ID
        first_message: The first message from the visitor
        user_email: Optional email of the visitor if collected
    """
    try:
        from_email = os.getenv("FROM_EMAIL")
        to_email = os.getenv("FROM_EMAIL")  # Send to yourself
        sendgrid_api_key = os.getenv("SENDGRID_API_KEY")

        if not sendgrid_api_key or not from_email:
            print("SendGrid not configured, skipping notification")
            return

        # Format the email content
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        subject = "🤖 New Digital Twin Engagement"

        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <h2 style="color: #2563eb;">New Visitor on Your Digital Twin</h2>
                <p>Someone just engaged with your digital twin chatbot!</p>

                <div style="background-color: #f3f4f6; padding: 15px; border-radius: 8px; margin: 20px 0;">
                    <p><strong>⏰ Time:</strong> {timestamp}</p>
                    <p><strong>🆔 Session ID:</strong> <code>{session_id}</code></p>
                    {f'<p><strong>📧 Visitor Email:</strong> {user_email}</p>' if user_email else ''}
                </div>

                <div style="background-color: #eff6ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
                    <p><strong>💬 First Message:</strong></p>
                    <p style="font-style: italic; color: #1e40af;">"{first_message}"</p>
                </div>

                <p style="color: #6b7280; font-size: 14px;">
                    You can view the full conversation history using the session ID.
                </p>
            </body>
        </html>
        """

        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )

        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)

        print(f"Notification sent successfully: {response.status_code}")
        return True

    except Exception as e:
        print(f"Failed to send notification: {str(e)}")
        return False
