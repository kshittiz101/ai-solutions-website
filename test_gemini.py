#!/usr/bin/env python
"""Test script to verify Gemini API connection"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def test_gemini_api():
    """Test Gemini API connection"""
    print("Testing Gemini API connection...")
    print("=" * 50)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY not found in .env file")
        return False

    print(f"✓ API Key found: {api_key[:10]}...{api_key[-4:]}")

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        print("✓ Client created successfully")
        print("\nTesting with a simple query...")

        response = client.chat.completions.create(
            model="gemini-1.5-flash-latest",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello in one sentence."}
            ]
        )

        ai_response = response.choices[0].message.content
        print(f"✓ API Response received:")
        print(f"  {ai_response}")
        print("\n✅ SUCCESS! Gemini API is working correctly.")
        return True

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        print("\nFull traceback:")
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    success = test_gemini_api()
    exit(0 if success else 1)

