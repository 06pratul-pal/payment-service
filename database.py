# Database Connection Manager
# WARNING: pool_size was changed to 5 in PR #2
# This is causing connection exhaustion

class ConnectionPool:
    def __init__(self, pool_size=20):  # Default was 20
        self.pool_size = pool_size
        self.connections = []
        self.used = 0
    
    def get_connection(self):
        if self.used >= self.pool_size:
            # LINE 13 - This is where crash happens
            raise Exception(
                f"DatabaseConnectionTimeout: "
                f"Pool exhausted ({self.used}/{self.pool_size})"
            )
        self.used += 1
        return Connection()

def get_connection(pool_size=20):
    pool = ConnectionPool(pool_size=pool_size)
    return pool.get_connection()

class Connection:
    def execute(self, query, params=None):
        return Result()

class Result:
    id = "TXN001"
    status = "success"
