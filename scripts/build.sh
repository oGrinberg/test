
#!/usr/bin/env sh

echo "The script you are running has:"
echo "basename: [$(basename "$0")]"
echo "dirname : [$(dirname "$0")]"
echo "pwd     : [$(pwd)]"


docker build $(dirname "$0")/../app/fastapi -t test/fastapi:1.0