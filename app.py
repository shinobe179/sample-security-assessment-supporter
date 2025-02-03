import asyncio
import streamlit as st
from textwrap import dedent
from browser_use import Agent
from langchain_openai import ChatOpenAI 
from pprint import pprint


def main():
    st.title('AI Supporter for Security Assessment')
    with st.form('url'):
        url = st.text_input('url')
        submitted = st.form_submit_button('チェックする')
    
    if submitted:
        result = setup_ai(url)
        st.markdown(f'```{result.action_results()[-1].extracted_content}```')


def setup_ai(url):
    llm = ChatOpenAI(model='gpt-4o-mini')
    task = dedent(f"""{url}は、あるWebサービスのWebサイトです。
                    このWebサービスの情報セキュリティに関するドキュメントを参照して、
                    ISMSやプライバシーマーク、FedLAMPなどのセキュリティ認証を取得しているかを確認してください。
                    結果は全て<answer>タグに含めて表示してください。
                    もし標準を取得していたら、取得している認証名を日本語かつカンマ区切りでリストアップし、
                    <answer>タグ内の<standards>タグに含めて表示してください。
                    また、参考にしたドキュメントのURLを<answer>タグ内の<refer>タグに含めて表示してください。
                    1つも取得していない場合は、<answer>タグのみ表示してください。""")
    agent = Agent(
        task=task,
        llm=llm,
    )
    async def query_ai():
        result = await agent.run()
        return result
    
    result = asyncio.run(query_ai())
    return result


if __name__ == "__main__":
    main()
