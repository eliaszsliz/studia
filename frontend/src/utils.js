export function truncateHtml(str, n) {
  const openTags = [];
  let inTag = false;
  const openTagsSafe = [];
  let tagName = '';
  let tagNameComplete = false;
  let tagClosing = false;
  let lastSpace = 0;
  for (let p = 0; p < str.length && p < n; p++) {
    const c = str.charAt(p);
    switch (c) {
      case '<':
        lastSpace = ((!inTag && p + 3 < n) ? p : lastSpace);
        inTag = true;
        tagName = '';
        tagNameComplete = false;
        break;
      case '>':
        if (inTag && !tagNameComplete) {
          openTags.push({
            tag: tagName,
            p,
          });
          tagNameComplete = true;
        }
        inTag = false;
        if (tagClosing) openTags.pop();
        tagClosing = false;
        tagName = ''; // may be redundant
        break;
      case '/':
        tagClosing = inTag;
        break;
      case ' ':
        lastSpace = ((!inTag && p + 3 < n) ? p : lastSpace);
        if (inTag && !tagNameComplete) {
          openTags.push({
            tag: tagName,
            p,
          });
          tagNameComplete = true;
        }
        break;
    }
    if (!tagNameComplete && c !== '<' && c !== '>') tagName += c;
  }
  // console.log(openTags, inTag, tagName, tagNameComplete, tagClosing, lastSpace);
  let small = `${str.substring(0, lastSpace)}...`;
  for (let i = openTags.length - 1; i >= 0; i--) { if (openTags[i].p <= lastSpace) small += `</${openTags[i].tag}>`; }
  return small;
}
