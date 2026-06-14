"""Helper utilities."""

import random
from typing import List, Dict, Any


def generate_request_id() -> str:
    """Generate unique request ID.
    
    Returns:
        Request ID string
    """
    return f"req_{random.randint(100000, 999999)}"


def chunk_list(lst: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks.
    
    Args:
        lst: List to chunk
        size: Chunk size
        
    Returns:
        List of chunks
    """
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple dictionaries.
    
    Args:
        *dicts: Dictionaries to merge
        
    Returns:
        Merged dictionary
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result
