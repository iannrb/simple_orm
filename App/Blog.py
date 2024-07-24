from connection_orm import Base, engine, session
from User import User
from Post import Post
import os, time

Base.metadata.create_all(engine)

def show_menu():
  print("Options menu:" +
        "\n1 - Add new user" +
        "\n2 - New post" +
        "\n3 - Search for Users and Posts" +
        "\n4 - Exit")
  
def add_user():
  os.system("cls")
  print("Add new user")
  name = input("Name: ")
  email = input("Email: ")
  user = User(name, email)
  session.add(user)
  session.commit()
  print("User added successfully")
  
def new_post():
  os.system("cls")
  print("Create new post")
  title = input("Title: ")
  content = input("Content: ")
  author_id = input("Author's ID: ")
  user = session.query(User).filter_by(id=author_id).first()
  
  if user:
    post = Post(title=title, content=content, author=user)
    session.add(post)
    session.commit()
    print("Post created successfully")
  
  else:
    print("User not found")
    
def query_users_posts():
  os.system("cls")
  users = session.query(User).join(User.posts).order_by(User.name).all()
  for user in users:
    print(f"User: {user.name} - Email: {user.email}")
    for post in user.posts:
      print(f"> Post title: {post.title} \n> Content: {post.content}\n")
    print("\n" + "-"*30 + "\n")