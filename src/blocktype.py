from enum import Enum


class BlockType(Enum):
	block_paragraph = "paragraph"
	block_heading = "heading"
	block_code = "code"
	block_quote = "quote"
	block_unordered_list = "unordered_list"
	block_ordered_list = "ordered_list"

def block_to_block_type(text):
	lines = text.split("\n")
	first_line = text.split("\n")[0]


	if text.startswith("#"):
		count = 0
		for char in text:
			if char == "#":
				count += 1
			else:
				break
		if 1 <= count <= 6:
			if count < len(text):
				if text[count] == " ":
					return BlockType.block_heading
	if  text.startswith("```\n") and text.endswith("```"):
		return BlockType.block_code
	if all(line.startswith(">") for line in lines):
		return BlockType.block_quote
	if all(line.startswith("- ") for line in lines):
		return BlockType.block_unordered_list
	else:
		for i, line in enumerate(lines):
			expected = str(i + 1) + ". "
			if not line.startswith(expected):
				return BlockType.block_paragraph
		return BlockType.block_ordered_list
			
	
	