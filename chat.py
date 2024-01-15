from ctransformers import AutoModelForCausalLM
llm = AutoModelForCausalLM.from_pretrained("chat.gguf")

while True:
      ask = input("Enter a Question (Q for quit): ")

      if ask == "q" or ask == "Q":
            break

      ans = llm(ask, max_new_tokens=1024)
      print(ask+ans)

print("Goodbye!")
