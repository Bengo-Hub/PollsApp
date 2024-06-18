# Building model relationships
## For auth management, user inbuilt django auth app(User model)

# Table structure
## 1. Candidates
- id,user(FK to User(id)),id_no,age,manifesto,background_info,post(FK to Posts(id))
## 2. Posts
- name,id
## 3. Voters
- id,user(FK to User(id)),id_no,age
## 4. Votes
- id,post(FK to POsts(id)),candidate(FK to Candidates(id)), voter(FK to Votes(id))