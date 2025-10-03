#!/usr/bin/env python
"""
Test database connection script
Run: pipenv run python test_db_connection.py
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection
from django.conf import settings

def test_connection():
    """Test database connection and display info"""
    print("=" * 60)
    print("🔍 Testing Database Connection")
    print("=" * 60)

    # Get database settings
    db_settings = settings.DATABASES['default']
    db_engine = db_settings.get('ENGINE', 'Unknown')

    print(f"\n📊 Database Configuration:")
    print(f"   Engine: {db_engine}")

    if 'postgresql' in db_engine:
        print(f"   Database: PostgreSQL")
        print(f"   Host: {db_settings.get('HOST', os.getenv('DATABASE_URL', 'N/A'))}")
    else:
        print(f"   Database: SQLite")
        print(f"   Path: {db_settings.get('NAME', 'N/A')}")

    print("\n🔄 Attempting connection...")

    try:
        # Test connection
        with connection.cursor() as cursor:
            # Get database version
            if 'postgresql' in db_engine:
                cursor.execute("SELECT version();")
                version = cursor.fetchone()[0]
                print(f"\n✅ Successfully connected to PostgreSQL!")
                print(f"\n📦 PostgreSQL Version:")
                print(f"   {version.split(',')[0]}")
            else:
                cursor.execute("SELECT sqlite_version();")
                version = cursor.fetchone()[0]
                print(f"\n✅ Successfully connected to SQLite!")
                print(f"\n📦 SQLite Version:")
                print(f"   {version}")

            # Check tables
            cursor.execute("""
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_schema = 'public'
            """ if 'postgresql' in db_engine else """
                SELECT COUNT(*)
                FROM sqlite_master
                WHERE type='table'
            """)
            table_count = cursor.fetchone()[0]
            print(f"\n📋 Database Tables: {table_count}")

            # Check Django migrations
            cursor.execute("""
                SELECT COUNT(*)
                FROM django_migrations
            """)
            migration_count = cursor.fetchone()[0]
            print(f"🔄 Applied Migrations: {migration_count}")

        print("\n" + "=" * 60)
        print("✅ Database connection test PASSED!")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\n❌ Connection failed!")
        print(f"\n🔥 Error: {type(e).__name__}")
        print(f"   {str(e)}")
        print("\n" + "=" * 60)
        print("❌ Database connection test FAILED!")
        print("=" * 60)

        # Troubleshooting tips
        print("\n💡 Troubleshooting Tips:")
        if 'postgresql' in db_engine:
            print("   1. Check DATABASE_URL is set correctly")
            print("   2. Verify PostgreSQL is running")
            print("   3. Check database credentials")
            print("   4. Ensure database allows remote connections")
        else:
            print("   1. Check database file exists")
            print("   2. Run: pipenv run python manage.py migrate")
            print("   3. Check file permissions")

        return False

if __name__ == '__main__':
    success = test_connection()
    sys.exit(0 if success else 1)

