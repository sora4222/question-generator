from chromadb import Collection
from notion_common.markdown import convert_to_markdown
from notion_common.pages import get_blocks, get_page_list


async def update_notion_collection(collection: Collection):
    """Fills ChromaDB with data from Notion."""
    page_list = await get_page_list()
    print(f"Fetched {len(page_list)} pages from Notion.")
    page_blocks = await get_blocks(page_list)
    markdown_pages = convert_to_markdown(page_blocks)
    ids, documents = map(list, zip(*markdown_pages.items()))
    collection.upsert(ids=ids, documents=documents)
