const authors = [
  {
    id: 0,
    slug:	'adam-nawalka',
    full_name: 'Adam Nawałka',
  },
  {
    id:	1,
    slug:	'janina-migdaek',
    full_name: 'Janina Migdałek',
  },
  {
    id:	4,
    slug:	'author-dwa',
    full_name: 'Author Dwa',
  },
];

const categories = [
  { name:	'Owoce', slug: 'owoce', id: 0 },
  { name:	'Jabłka', slug: 'jabka', id: 1 },
  { name:	'Gruszki', slug: 'gruszki', id: 2 },
];

const issues = [
  {
    id: 1,
    date: 2010,
  },
  {
    id: 2,
    date: 2011,
  },
];

const articles = [
  {
    id: 0,
    belong_to: issues[0],
    title: 'TEST123',
    slug: 'test123',
    body: 'Adfasdf asdf asdfasdf wre yweufhgbddfbgf fj .',
    authors: [
      authors[0],
    ],
    categories: [
      categories[0], categories[1],
    ],
    created_at: '2017-12-07',
  },
  {
    id: 1,
    belong_to: issues[1],
    title: 'SADFASFD',
    slug: 'sadfasefd',
    body: 'gasdfgsa yweufhgbddfbgf fj .',
    authors: [
      authors[1], authors[2],
    ],
    categories: [
      categories[2],
    ],
    created_at: '2016-11-02',
  },
  {
    id: 2,
    belong_to: issues[1],
    title: 'Psdf gdsf gdsfgvbcxvcxvbxcv',
    slug: 'psdf-gdsf-gdsfgvbcxvcxvbxcv',
    body: 'jdf asdf asdfasdf wre yweufhgbddfbgf fj .',
    authors: [
      authors[0],
    ],
    categories: [
      categories[0], categories[1],
    ],
    created_at: '2017-12-07',
  },
];

export {
  articles,
  authors,
  categories,
  issues,
};
