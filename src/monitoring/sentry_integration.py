def init_sentry(dsn):
    import sentry_sdk
    sentry_sdk.init(dsn=dsn)