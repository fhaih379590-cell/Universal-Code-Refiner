import os, glob
from openai import OpenAI

# 初始化客户端
# client = OpenAI(api_key=os.getenv("LLM_API_KEY"))
client = OpenAI(
    base_url="https://models.inference.ai.azure.com", # 增加这一行
    api_key=os.getenv("LLM_API_KEY")
)
def refine_all_languages():
    # 确保输出目录存在
    os.makedirs("data/output", exist_ok=True)
    
    # 获取 input 目录下所有文件
    files = glob.glob("data/input/**/*.*", recursive=True)
    
    if not files:
        print("No files found in data/input/")
        return

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        print(f"Processing: {file_path}")
        
        prompt = f"""
        你是一个代码提纯专家。请将以下语料转化为高质量数据：
        1. 修复 Bug、重构复杂逻辑、提升可读性。
        2. 脱敏：删除所有 IP、密钥、内部敏感信息。
        3. 增强：补全 JSDoc/Docstring 规范注释。
        4. 解释：在代码最下方增加一个 '### Reasoning' 部分，说明你的治理逻辑。
        
        代码语料如下：
        {code}
        """
        
        try:
            result = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            ).choices[0].message.content

            output_path = file_path.replace("data/input", "data/output")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    refine_all_languages()
