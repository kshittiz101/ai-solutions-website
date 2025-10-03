from django.utils.text import slugify
import uuid
from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logger = logging.getLogger(__name__)

def generate_slug(title: str, class_name: str) -> str:
    title = slugify(title)
    while class_name.objects.filter(slug=title).exists():
        title = f"{title}-{uuid.uuid4().hex[:4]}"
    return title




def get_company_context():
    """Fetch company data from database for AI context"""
    from .models import Service, CaseStudy, Article, Event

    # Get services
    services = Service.objects.filter(status='active')[:6]
    services_info = "\n".join([
        f"- {s.title}: {s.short_description}"
        for s in services
    ]) if services.exists() else "AI/ML Services, NLP Solutions, Computer Vision"

    # Get case studies
    case_studies = CaseStudy.objects.all()[:3]
    case_studies_info = "\n".join([
        f"- {cs.title}: {cs.summary}"
        for cs in case_studies
    ]) if case_studies.exists() else "Multiple successful AI implementation projects"

    return f"""
SERVICES WE OFFER:
{services_info}

SUCCESS STORIES:
{case_studies_info}

CONTACT INFORMATION:
- Website: Visit /contact/ page for inquiry form
- Services Page: /services/
- Case Studies: /case-study/
- Articles: /articles/
- Events: /events/
"""

SYSTEM_PROMPT = """
You are an AI assistant for AI Solutions, a leading AI development company specializing in custom AI solutions for businesses.

COMPANY OVERVIEW:
AI Solutions helps organizations leverage artificial intelligence to solve complex problems and drive growth. We provide:
- AI Strategy & Consulting
- Machine Learning Development
- Natural Language Processing
- Computer Vision Solutions
- AI Integration & Deployment
- Advanced Data Analytics

YOUR ROLE:
1. Answer questions about AI Solutions' services, case studies, and capabilities
2. Provide helpful information about how AI can benefit businesses
3. Guide users to relevant pages (services, case studies, contact, etc.)
4. Be professional, friendly, and informative
5. If asked about topics unrelated to AI Solutions or AI technology, politely say you can only help with questions about AI Solutions and AI technologies

IMPORTANT:
- Format responses using HTML tags: <strong>, <br/>, <ul>, <li>, etc.
- Use links like: <a href="/services/" class="text-emerald-400 underline">Services page</a>
- Be concise but informative
- Always maintain a helpful and professional tone
- If you don't have specific information, direct users to contact the team

{company_context}
"""


AI_MODLE_ID="gemini-2.0-flash",
def generate_gemini_response(query: str) -> str:
    """Generate AI response using Gemini API with company context"""
    try:
        # Get fresh company context
        company_context = get_company_context()

        # Format system prompt with context
        formatted_prompt = SYSTEM_PROMPT.format(company_context=company_context)

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            logger.error("GEMINI_API_KEY not found in environment variables")
            raise ValueError("API key not configured")

        logger.debug(f"Using API key: {api_key[:10]}...")
        logger.debug(f"Query received: {query}")

        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        response = client.chat.completions.create(
            model=AI_MODLE_ID,
            messages=[
                {"role": "system", "content": formatted_prompt},
                {"role": "user", "content": query}
            ]
        )

        ai_response = response.choices[0].message.content
        logger.debug(f"AI Response: {ai_response[:100]}...")

        return ai_response

    except Exception as e:
        # Log the full error
        import traceback
        logger.error(f"ERROR in generate_gemini_response: {str(e)}")
        logger.error(traceback.format_exc())

        # Fallback response if Gemini API fails
        return f"""I apologize, but I'm having trouble connecting to the AI service right now. 🤖<br/><br/>
        In the meantime, you can:<br/><br/>
        • Visit our <a href="/services/" class="text-emerald-400 underline">Services page</a> to learn about our offerings<br/>
        • Check out our <a href="/case-study/" class="text-emerald-400 underline">Case Studies</a> to see our success stories<br/>
        • <a href="/contact/" class="text-emerald-400 underline">Contact us</a> directly for personalized assistance<br/><br/>
        Technical error: {str(e)[:200]}"""

