#!/usr/bin/env python3
import os
import sys
import re
from dotenv import load_dotenv
from src.bot import run_discord_bot
from src.log import logger

load_dotenv()

def validate_discord_token(token: str) -> bool:
    """Validate Discord bot token format"""
    if not token:
        return False
    
    # Discord bot tokens are typically in the format "Bot XXXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # But for simplicity, we'll just check if it's a reasonable length and contains only valid characters
    if len(token) < 50 or len(token) > 100:
        return False
    
    # Basic regex check for token format (this is a simplified check)
    # Real tokens have specific patterns but we'll keep it simple
    return bool(re.match(r'^[A-Za-z0-9_.-]+
, token))

def validate_environment():
    """Validate required environment variables"""
    required_vars = ["DISCORD_BOT_TOKEN"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please check your .env file")
        return False
    
    # Validate Discord token format
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    if not validate_discord_token(discord_token):
        logger.warning("Discord bot token may be invalid. Please check the format.")
        # We'll continue anyway but warn the user
    
    providers = []
    if os.getenv("OPENAI_KEY"):
        providers.append("OpenAI")
    if os.getenv("CLAUDE_KEY"):
        providers.append("Claude")
    if os.getenv("GEMINI_KEY"):
        providers.append("Gemini")
    if os.getenv("GROK_KEY"):
        providers.append("Grok")
    
    providers.append("Free (always available)")
    
    logger.info(f"Available providers: {', '.join(providers)}")
    
    return True

def main():
    """Main entry point"""
    logger.info("Starting Discord AI Bot...")
    
    if not validate_environment():
        logger.error("Environment validation failed. Exiting.")
        sys.exit(1)
    
    logger.info("Environment validation passed")
    
    try:
        run_discord_bot()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Bot crashed with unhandled exception: {e}")
        logger.exception("Full traceback:")
        sys.exit(1)

if __name__ == "__main__":
    main()
