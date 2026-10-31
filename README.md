# SoloPulse

Minimal, zero-dependency health monitor and static status page generator for solo SaaS founders and indie hackers.

**Signature: Mourad.Soltani**

## Why SoloPulse?

In 2026, solo founders need lightweight uptime visibility without Datadog bills or complex setups. SoloPulse checks your critical endpoints and generates a clean static HTML status page you can host anywhere (GitHub Pages, S3, etc.).

Trending niche: Indie/micro-SaaS status & uptime tools.

## Features

- Zero external dependencies (Python stdlib only)
- Check multiple HTTP endpoints
- Generate responsive static status HTML
- Latency and status reporting
- Easy JSON config

## Quick Start

```bash
# Create config.json
cat > config.json << 'EOF'
{
  "title": "My SaaS Status",
  "endpoints": [
    {"name": "API", "url": "https://api.yoursite.com/health"},
    {"name": "Website", "url": "https://yoursite.com"}
  ]
}
EOF

python solopulse.py --config config.json --output status.html
```

Open `status.html` in a browser.

## Tests

```bash
python -m pytest tests/  # or
python -m unittest tests.test_health
```

All health tests must pass.

## License

MIT — see LICENSE

Built by Mourad.Soltani
