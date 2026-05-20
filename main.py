import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function 


def get_client():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None: 
        raise RuntimeError("api_key wasn't found")
    return genai.Client(api_key=api_key)

def parse_args():
    parser = argparse.ArgumentParser(description="AI-Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

def print_formatter(prompt, prompt_tokens, candidate_tokens, response_text, response_function_calls, verbose_flag):
    if verbose_flag:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {candidate_tokens}")
    functions_results = []
    if response_function_calls is not None:
        for function_call in response_function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call)
            if not function_call_result.parts:
                raise Exception("Error: function call returned an empty list")
            if function_call_result.parts[0].function_response is None:
                raise Exception("Error: function call returned a None value FunctionResponse object")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Error: function call returned a None value FunctionResponse.response")
            functions_results.append(function_call_result.parts[0]) 
            if verbose_flag:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    print(f"Response:\n   {response_text}")


def main():
    client = get_client()
    current_model="gemini-flash-latest"
    # current_model="gemini-2.5-flash"

    args = parse_args()
    prompt = args.user_prompt
    verbose_flag = args.verbose

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = client.models.generate_content(
        model=current_model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )
    if response.usage_metadata == None:
        raise RuntimeError("response.usage_metadata is None, likely to failed API request")
    prompt_tokens = response.usage_metadata.prompt_token_count
    candidate_tokens = response.usage_metadata.candidates_token_count
    print_formatter(
        prompt, 
        prompt_tokens, 
        candidate_tokens, 
        response.text, 
        response.function_calls, 
        verbose_flag
    )

if __name__ == "__main__":
    main()
