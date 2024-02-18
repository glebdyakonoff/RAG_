#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 07:49:18 2024

@author: gleb
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from abc import ABC, abstractmethod
from typing import Any, Sequence

class Document(BaseModel):
    """Class for storing a piece of text and associated metadata."""

    page_content: str
    """String text."""
    metadata: dict = Field(default_factory=dict)
    """Arbitrary metadata about the page content (e.g., source, relationships to other
        documents, etc.).
    """
    
class BaseDocumentTransformer(ABC):
    """Abstract base class for document transformation systems.

    A document transformation system takes a sequence of Documents and returns a
    sequence of transformed Documents.


    """  
    @abstractmethod
    def transform_documents(
        self, documents: Sequence[Document], **kwargs: Any
    ) -> Sequence[Document]:
        """Transform a list of documents.

        Args:
            documents: A sequence of Documents to be transformed.

        Returns:
            A list of transformed Documents.
        """