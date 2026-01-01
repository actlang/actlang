import asyncio
from actlang.core.agent import Agent
from tools.actlang.pdf_loader.pdf_loader import PDFLoader
from tools.actlang.llamaindex_chunker.chunker import Chunker

async def main():
    agent = Agent([PDFLoader(), Chunker()])
    result = await agent.run()
    print(result.data)

asyncio.run(main())
