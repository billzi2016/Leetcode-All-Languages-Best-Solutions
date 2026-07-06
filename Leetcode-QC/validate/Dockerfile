FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        build-essential \
        default-jdk \
        nodejs \
        npm \
        golang-go \
        rustc \
        cargo \
        ruby-full \
        php-cli \
        mono-devel \
        scala \
        kotlin \
        racket \
        erlang \
        elixir \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY Leetcode-QC/validate/requirements.txt /tmp/validate-requirements.txt
RUN pip install --no-cache-dir -r /tmp/validate-requirements.txt

CMD ["python", "Leetcode-QC/validate/run_validation.py", "--repo-root", "/workspace"]
