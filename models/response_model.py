# from typing import List, Optional
# from pydantic import BaseModel
#
# class Metadata(BaseModel):
#     title: Optional[str]
#     author: Optional[str]
#     subject: Optional[str]
#     keywords: Optional[str]
#     producer: Optional[str]
#     creationDate: Optional[str]
#
# class ExtractedDataResponse(BaseModel):
#     text: str
#     images: List[str]
#     metadata: Metadata

# 2----------------------------------------------------------
# # models/response_model.py
# from typing import List, Optional
# from pydantic import BaseModel
#
# class Metadata(BaseModel):
#     title: Optional[str]
#     author: Optional[str]
#     subject: Optional[str]
#     keywords: Optional[str]
#     producer: Optional[str]
#     creationDate: Optional[str]
#
# class ExtractedDataResponse(BaseModel):
#     text: str
#     images: List[str]
#     metadata: Metadata


# 3----------------------------------------------------------
# models/response_model.py
# from typing import List, Optional
# from pydantic import BaseModel
#
# class Metadata(BaseModel):
#     pdf_name: str
#     pdf_size: int
#     num_pages: int
#     language: str
#     chapters: List[str]
#     title: Optional[str]
#     author: Optional[str]
#     subject: Optional[str]
#     keywords: Optional[str]
#     producer: Optional[str]
#     creationDate: Optional[str]
#
# class ExtractedDataResponse(BaseModel):
#     text: str
#     images: List[str]
#     metadata: Metadata
#     chapters_extracted: List[str]
#     pages_extracted: List[int]

# 4----------------------------------------------------------
# models/response_model.py
# from typing import List, Optional
# from pydantic import BaseModel
#
# class Metadata(BaseModel):
#     pdf_name: str
#     pdf_size: int
#     num_pages: int
#     language: str
#     chapters: List[str]
#     title: Optional[str] = "No data found"
#     author: Optional[str] = "No data found"
#     subject: Optional[str] = "No data found"
#     keywords: Optional[str] = "No data found"
#     producer: Optional[str] = "No data found"
#     creationDate: Optional[str] = "No data found"
#
# class ExtractedDataResponse(BaseModel):
#     text: str
#     images: List[str]
#     metadata: Metadata
#     chapters_extracted: List[str]
#     pages_extracted: List[int]


# 5----------------------------------------------------------
# models/response_model.py
# from typing import List, Optional
# from pydantic import BaseModel
#
# class Metadata(BaseModel):
#     pdf_name: str
#     pdf_size: int
#     num_pages: int
#     language: str
#     chapters: List[str]
#     title: Optional[str] = "No data found"
#     author: Optional[str] = "No data found"
#     subject: Optional[str] = "No data found"
#     keywords: Optional[str] = "No data found"
#     producer: Optional[str] = "No data found"
#     creationDate: Optional[str] = "No data found"
#
# class ExtractedDataResponse(BaseModel):
#     text: str
#     images: List[str]
#     metadata: Metadata
#     chapters_extracted: List[str]
#     pages_extracted: List[int]

# 2 -> 6----------------------------------------------------------
# models/response_model.py
from typing import List, Optional
from pydantic import BaseModel

class Metadata(BaseModel):
    title: Optional[str]
    author: Optional[str]
    subject: Optional[str]
    keywords: Optional[str]
    producer: Optional[str]
    creationDate: Optional[str]

class ExtractedDataResponse(BaseModel):
    text: str
    images: List[str]
    metadata: Metadata
    notes: Optional[str]  # Optional field for loss or notes in extraction
