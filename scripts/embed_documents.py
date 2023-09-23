import argparse

from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Qdrant


def embed_document(document_path: str, qdrant_path: str) -> str:
    loader = TextLoader(document_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    qdrant = Qdrant.from_documents(
        docs,
        embeddings,
        path=qdrant_path,
        collection_name="my_documents",
        # the collection is going to be reused if it already exists
        # https://python.langchain.com/docs/integrations/vectorstores/qdrant#recreating-the-collection
        # force_recreate=False,
    )

    query = "What did the president say about Ketanji Brown Jackson"
    found_docs = qdrant.similarity_search_with_score(query)

    # print(found_docs[0])
    document, score = found_docs[0]
    print(document.page_content)
    print(f"\nScore: {score}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--document-path",
        help="file path for document",
        type=str,
        default="./samples/state_of_the_union.txt",
    )
    parser.add_argument(
        "--qdrant-path",
        help="file path for qdrant on-disk storage",
        type=str,
        default="./local_qdrant",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    embed_document(args.document_path, args.qdrant_path)
