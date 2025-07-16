# Use a specific Python version for reproducibility
FROM python:3.12-slim-bookworm AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_HOME=/.uv

# Install system dependencies, including SSH server
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Install uv, a fast Python package installer
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user for security
RUN useradd -ms /bin/bash dev
USER dev
WORKDIR /home/dev/app

# --- SSH Configuration ---
# Create SSH directory for the 'dev' user
RUN mkdir -p /home/dev/.ssh
# Copy the user's public key to the container.
# IMPORTANT: You must place your public SSH key (e.g., id_rsa.pub)
# inside the 'config/ssh/' directory on your local machine.
COPY --chown=dev:dev config/ssh/ /home/dev/.ssh/authorized_keys
# Set correct permissions
RUN chmod 700 /home/dev/.ssh && \
    chmod 600 /home/dev/.ssh/authorized_keys

# Copy project files
COPY --chown=dev:dev . .

# Install Python dependencies using uv
# This runs as the 'dev' user
RUN /root/.cargo/bin/uv pip install -r requirements.txt

# Expose the SSH port
EXPOSE 22

# Start the SSH server as the main command
CMD ["/usr/sbin/sshd", "-D"]