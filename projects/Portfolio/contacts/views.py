# contacts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import ContactMessage
from .utils import send_email_notification

class ContactView(FormView):
    template_name = 'contacts/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts:contact')
    
    def form_valid(self, form):
        # Save the contact message
        contact_message = form.save()
        
        # Send email notification to Admin
        subject = f"New Contact Message from {contact_message.name}"
        message_body = (
            f"You have received a new contact message.\n\n"
            f"Name: {contact_message.name}\n"
            f"Email: {contact_message.email}\n"
            f"Subject: {contact_message.subject}\n\n"
            f"Message:\n{contact_message.message}"
        )
        
        try:
            send_email_notification(
                subject=subject,
                message=message_body,
                recipient=None  # Defaults to admin/EMAIL_HOST_USER
            )
        except Exception as e:
            print(f"Error sending email: {e}")
        
        # Add success message
        messages.success(
            self.request,
            'Thank you for your message! I will get back to you soon.'
        )
        
        return super().form_valid(form)