from openai.resources.embeddings import Embeddings
from openai._types import NotGiven, NOT_GIVEN
from openai.types.create_embedding_response import CreateEmbeddingResponse, Usage
from openai.types.embedding import Embedding
from openai import OpenAI

from typing import Union, List, Literal, Any

from core.model_runtime.errors.invoke import InvokeAuthorizationError

import re

class MockEmbeddingsClass(object):
    def create_embeddings(
        self: Embeddings, *,
        input: Union[str, List[str], List[int], List[List[int]]],
        model: Union[str, Literal["text-embedding-ada-002"]],
        encoding_format: Literal["float", "base64"] | NotGiven = NOT_GIVEN,
        **kwargs: Any
    ) -> CreateEmbeddingResponse:
        if isinstance(input, str):
            input = [input]

        if not re.match(r'^(https?):\/\/[^\s\/$.?#].[^\s]*$', self._client.base_url.__str__()):
            raise InvokeAuthorizationError('Invalid base url')
        
        if len(self._client.api_key) < 18:
            raise InvokeAuthorizationError('Invalid API key')
        
        if encoding_format == 'float':
            return CreateEmbeddingResponse(
                data=[
                    Embedding(
                        embedding=[0.23333 for _ in range(233)],
                        index=i,
                        object='embedding'
                    ) for i in range(len(input))
                ],
                model=model,
                object='list',
                # marked: usage of embeddings should equal the number of testcase
                usage=Usage(
                    prompt_tokens=2,
                    total_tokens=2
                )
            )
        
        embeddings = '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'

        data = []
        for i, text in enumerate(input):
            obj = Embedding(
                embedding=[],
                index=i,
                object='embedding'
            )
            obj.embedding = embeddings

            data.append(obj)

        return CreateEmbeddingResponse(
            data=data,
            model=model,
            object='list',
            # marked: usage of embeddings should equal the number of testcase
            usage=Usage(
                prompt_tokens=2,
                total_tokens=2
            )
        )