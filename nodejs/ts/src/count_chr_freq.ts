function countCharacters(str: string): Record<string, number> {
    const count: Record<string, number> = {};

    for (const c of str) {
        count[c] = (count[c] || 0) + 1;
    }

    return count
}

function sortCharactersByFrequency(str: string): string[] {
  const charFrequency = countCharacters(str);
  const sortedChars = Object.keys(charFrequency).sort((a, b) => {
    return charFrequency[b] - charFrequency[a];
  });
  return sortedChars;
}

const str: string = "hello world"



console.log(countCharacters(str))
console.log(sortCharactersByFrequency(str))
