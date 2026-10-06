string1="""Bridge over Troubled Water
… When you're weary, feeling small,
When tears are in your eyes, I will dry them all;
I'm on your side. When times get rough
And friends just can't be found,
Like a bridge over troubled water
I will lay me down.
Like a bridge over troubled water
I will lay me down.
… When you're down and out,
When you're on the street,
When evening falls so hard
I will comfort you.
I'll take your part.
When darkness comes
And pain is all around,
Like a bridge over troubled water
I will lay me down.
Like a bridge over troubled water
I will lay me down.
… Sail on silvergirl,
Sail on by.
Your time has come to shine.
All your dreams are on their way.
See how they shine.
If you need a friend
I'm sailing right behind.
Like a bridge over troubled water
I will ease your mind.
Like a bridge over troubled water
I will ease your mind."""

import re


def analyze_lyrics(lyrics, word):
	if not word:
		return []

	pattern = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
	return [match.start() for match in pattern.finditer(lyrics)]


bridge_positions = analyze_lyrics(string1, "bridge")
print(bridge_positions)