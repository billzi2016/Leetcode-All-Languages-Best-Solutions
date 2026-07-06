FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/workspace/Leetcode-QC/validate-pro/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        build-essential \
        default-jdk \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY Leetcode-QC/validate-pro/requirements.txt /tmp/validate-pro-requirements.txt
RUN pip install --no-cache-dir -r /tmp/validate-pro-requirements.txt

CMD ["python", "Leetcode-QC/validate-pro/run_validation.py", "--repo-root", "/workspace"]
