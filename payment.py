# Payment Processing Service
# Version: 2.1.0
# Last modified: 2026-05-30

import database
import logging

# ==========================================
# DATABASE CONFIGURATION
# BUG INTRODUCED IN PR #2 - 2026-05-30
# ==========================================

DB_CONFIG = {
    "host": "prod-db.payfast.internal",
    "port": 5432,
    "name": "payments_db",
    "pool_size": 5,        # BUG! Was 20 before PR #2
    "max_overflow": 0,     # BUG! Was 10 before PR #2
    "timeout": 30
}

def process_payment(user_id, amount, card_token):
    """
    Process a payment transaction.
    BROKEN since PR #2 merged at 10:28 AM
    """
    try:
        # This fails because pool_size=5 gets exhausted
        conn = database.get_connection(
            pool_size=DB_CONFIG["pool_size"]  # LINE 28 - ROOT CAUSE
        )
        
        result = conn.execute(
            "INSERT INTO transactions VALUES (?, ?, ?)",
            [user_id, amount, card_token]
        )
        return {"status": "success", "txn_id": result.id}
        
    except Exception as e:
        logging.error(f"Payment failed: {e}")
        raise

def refund_payment(txn_id):
    """Process a refund"""
    conn = database.get_connection(
        pool_size=DB_CONFIG["pool_size"]
    )
    return conn.execute("UPDATE transactions SET status='refunded'")
