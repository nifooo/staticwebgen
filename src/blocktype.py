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


	if first_line.startswith("#"):
		count = 0
		for char in first_line:
			if char == "#":
				count += 1
			else:
				break
		if 1 <= count <= 6:
			if count < len(first_line):
				if first_line[count] == " ":
					return BlockType.block_heading
	if  text.startswith("```\n") and text.endswith("```"):
		return BlockType.block_code
	if all(line.startswith(">") for line in lines):
		return BlockType.block_quote
	if all(line.startswith("- ") for line in lines):
		return BlockType.block_unordered_list
	for i, line in enumerate(lines):
		expected = str(i + 1) + ". "
		if not line.startswith(expected):
			break
	else:
		return BlockType.block_ordered_list
	return BlockType.block_paragraph
			
	
	