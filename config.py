# Database Configuration
# WARNING: Pool size was changed from 20 to 5
# This caused production outage on 2026-05-30

DB_HOST = "prod-db.payment-service.internal"
DB_PORT = 5432
DB_NAME = "payments"
DB_POOL_SIZE = 20  # FIXED: restored from 5 to 20
DB_TIMEOUT = 30

# Payment Gateway
PAYMENT_GATEWAY_URL = "https://api.razorpay.com/v1"
MAX_RETRIES = 3
