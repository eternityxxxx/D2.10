# D2.10

<p>Чтобы проверить, что сервер действительно инегрирует с Sentry IO, нужно стянуть репозиторий к себе, и вот в этом месте: </p>
<code>
sentry_sdk.init(
    dsn="https://5b9737fb36de46ae9f6839efcbb1076d@o425255.ingest.sentry.io/5358991",
    integrations=[BottleIntegration()]
)
</code>
