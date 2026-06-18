#!/bin/bash
# Extract all project zip files

echo "🔄 Extracting projects..."

# Extract coskip-blog-api
unzip -q coskip-blog-api-main.zip -d temp_blog_api
if [ -d "temp_blog_api" ]; then
    # Find the actual project root (handle nested directories)
    if [ -d "temp_blog_api/coskip-blog-api-main" ]; then
        mv temp_blog_api/coskip-blog-api-main coskip-blog-api
        rm -rf temp_blog_api
    else
        mv temp_blog_api coskip-blog-api
    fi
    echo "✓ Extracted coskip-blog-api"
fi

# Extract coskip-bytes
unzip -q coskip-bytes-ayush-dev.zip -d temp_bytes
if [ -d "temp_bytes" ]; then
    # Find the actual project root (handle nested directories)
    if [ -d "temp_bytes/coskip-bytes-ayush-dev" ]; then
        mv temp_bytes/coskip-bytes-ayush-dev coskip-bytes
        rm -rf temp_bytes
    else
        mv temp_bytes coskip-bytes
    fi
    echo "✓ Extracted coskip-bytes"
fi

# Extract AI service
unzip -q ai.coskip.com-dev.zip -d temp_ai
if [ -d "temp_ai" ]; then
    if [ -d "temp_ai/ai.coskip.com-dev" ]; then
        mv temp_ai/ai.coskip.com-dev ai-service
        rm -rf temp_ai
    else
        mv temp_ai ai-service
    fi
    echo "✓ Extracted ai-service"
fi

echo "✅ All projects extracted successfully!"
echo ""
echo "📁 Directory structure:"
ls -la | grep "^d" | grep -E "(coskip|ai)"
