from Blog import show_menu, add_user, new_post, query_users_posts
import os, time

while True:
  show_menu()
  choice = int(input("\nSelect an option: (1-4)\n> "))
  
  match (choice): 
    case 1:
      add_user()
      time.sleep(1)
    case 2:
      new_post()
      time.sleep(1)
    case 3:
      query_users_posts()
      time.sleep(3)
    case 4:
      os.system("cls")
      print("Exiting...")
      break
    case _:
      os.system("cls")
      print("Invalid option!")
      time.sleep(0.5)