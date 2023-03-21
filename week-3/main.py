import json
import tkinter as tk
from tkinter import messagebox, ttk
from uuid import uuid4


class AddressBook:
    name: str
    address: str
    phone: str
    email: str
    id: str

    def __init__(self, name: str, address: str, phone: str, email: str, id: str = None) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.id = id or str(uuid4())[0:4]

    def __str__(self) -> str:
        return f"{self.name} lives at {self.address} and can be reached at {self.phone} or {self.email}."

    def __repr__(self) -> str:
        return f"AddressBook({self.name}, {self.address}, {self.phone}, {self.email})"

    def save(self):
        with open("addressbook.json", "r") as f:
            data = json.load(f)
            data.append(self.__dict__)

        with open("addressbook.json", "w") as f:
            json.dump(data, f, indent=4)

        # TODO: check if the contact already exists

    def delete(self):

        with open("addressbook.json", "r") as f:
            data = json.load(f)
            for i, contact in enumerate(data):
                if contact['id'] == self.id:
                    data.pop(i)

        with open("addressbook.json", "w") as f:
            json.dump(data, f, indent=4)

    def update(self):
        with open("addressbook.json", "r") as f:
            data = json.load(f)
            for contact in data:
                if contact["id"] == self.id:
                    contact["name"] = self.name
                    contact["address"] = self.address
                    contact["phone"] = self.phone
                    contact["email"] = self.email

        with open("addressbook.json", "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def search(search_val):
        results = []
        with open("addressbook.json", "r") as f:
            data = json.load(f)
            for contact in data:
                if search_val == '' or search_val.lower() in contact["name"].lower():
                    results.append(AddressBook(**contact))
            return results

    @staticmethod
    def load():
        with open("addressbook.json", "r") as f:
            data = json.load(f)
            return [AddressBook(**contact) for contact in data]


class MyGUI:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Address Book")
        self.window.geometry("800x600")
        self.detail_window = None

        # add menu
        self.menu = tk.Menu(self.window)

        # add search menu
        self.search_menu = tk.Menu(self.menu, tearoff=0)
        self.search_menu.add_command(
            label="Search by Name", command=self.search)

        self.menu.add_cascade(label="Menu", menu=self.search_menu)

        self.window.config(menu=self.menu)

        self.form_frame, self.name_entry, self.address_entry, self.phone_entry, self.email_entry = self.add_form_field()

        # end of form frame
        self.form_frame.pack(fill="x", padx=10, pady=10)

        # add submit button
        self.submit_button = tk.Button(
            self.window, text="Submit", command=self.add)
        self.submit_button.pack(padx=10, pady=10)

        # search input field bind with search function
        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack(padx=10, pady=10)
        self.search_entry.bind("<Return>", self.search)
        
        # search button
        self.search_button = tk.Button(
            self.window, text="Search", command=self.search)
        self.search_button.pack(padx=10, pady=10)
        # bind
        self.search_button.bind("<Return>", self.search)
        
        # Address Table
        self.table_frame = tk.Frame(self.window)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        address_books = AddressBook.load()

        self.tree = self.add_table(address_books)

        self.window.mainloop()

    def add_table(self, address_books: AddressBook):
        columns = ("id", "name", "address", "phone", "email")
        # scrollable treeview
        tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, width=100)
        for address_book in address_books:
            tree.insert("", "end", values=(
                address_book.id, address_book.name, address_book.address, address_book.phone, address_book.email))
        # limit the height of the treeview to 10 rows
        tree["height"] = 3
        tree.pack(fill="both", expand=True)
        tree.bind('<<TreeviewSelect>>', self.column_click)
        return tree

    def add_form_field(self, master=None, address=None, update=False):
        master = master or self.window
        # add form frame and widgets
        form_frame = tk.Frame(master)
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        # have small padding between the labels and the entry fields
        form_frame.columnconfigure(2, minsize=10)

        # add name label and entry field
        name_label = tk.Label(form_frame, text="Name")
        name_label.grid(row=0, column=0, sticky="e")
        name_entry = tk.Entry(form_frame)
        if address:
            name_entry.insert(0, address.name)
        name_entry.grid(row=0, column=1, sticky="w")

        # add address label and entry field
        address_label = tk.Label(form_frame, text="Address")
        address_label.grid(row=1, column=0, sticky="e")
        address_entry = tk.Entry(form_frame)
        if address:
            address_entry.insert(0, address.address)
        address_entry.grid(row=1, column=1, sticky="w")

        # add phone label and entry field
        phone_label = tk.Label(form_frame, text="Phone")
        phone_label.grid(row=2, column=0, sticky="e")
        phone_entry = tk.Entry(form_frame)
        if address:
            phone_entry.insert(0, address.phone)
        phone_entry.grid(row=2, column=1, sticky="w")

        # add email label and entry field
        email_label = tk.Label(form_frame, text="Email")
        email_label.grid(row=3, column=0, sticky="e")
        email_entry = tk.Entry(form_frame)
        if address:
            email_entry.insert(0, address.email)
        email_entry.grid(row=3, column=1, sticky="w")

        return form_frame, name_entry, address_entry, phone_entry, email_entry

    def add(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not address or not phone or not email:
            messagebox.showerror("Error", "Please fill all the fields")
            return

        address_book = AddressBook(name, address, phone, email)
        address_book.save()

        self.tree.insert("", "end", values=(
            address_book.id, address_book.name, address_book.address, address_book.phone, address_book.email))

        self.name_entry.delete(0, "end")
        self.address_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")

        # remove the focus from the submit button
        self.submit_button.focus()

    def search(self, event=None):
        search_val = self.search_entry.get()

        address_books = AddressBook.search(search_val)
        self.tree.delete(*self.tree.get_children())
        for address_book in address_books:
            self.tree.insert("", "end", values=(
                address_book.id, address_book.name, address_book.address, address_book.phone, address_book.email))
            
        

    def column_click(self, event):
        if not messagebox.askokcancel("Update", "Do you want to update?"):
            return
        print(event)
        try:
            item_selected = self.tree.selection()[0]
            item = self.tree.item(item_selected)

            address = AddressBook(id=item["values"][0], name=item["values"][1],
                                  address=item["values"][2], phone=item["values"][3], email=item["values"][4])
            self.detail_view(address)
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()

    def detail_view(self, address):
        self.detail_window = tk.Toplevel(self.window)
        self.detail_address = address
        self.detail_window.title("Detail View")
        self.detail_window.geometry("400x300")

        self.detail_form_frame, self.detail_name_entry, self.detail_address_entry, self.detail_phone_entry, self.detail_email_entry = self.add_form_field(
            self.detail_window, address, True)
        self.detail_form_frame.pack(fill="both", expand=True, padx=10, pady=10)

        update_button = tk.Button(self.detail_window, text="Update",
                                  command=self.update)
        update_button.pack(side="left", padx=10, pady=10)

        # with red text
        delete_button = tk.Button(self.detail_window, text="Delete",
                                  command=self.delete, fg="red")
        delete_button.pack(side="left", padx=10, pady=10)

        self.detail_window.mainloop()

    def update(self):
        if not self.detail_address:
            messagebox.showerror("Error", "Please select an item to update")
            return

        self.detail_address.name = self.detail_name_entry.get()
        self.detail_address.address = self.detail_address_entry.get()
        self.detail_address.phone = self.detail_phone_entry.get()
        self.detail_address.email = self.detail_email_entry.get()

        self.detail_address.update()

        self.detail_window.destroy()
        self.detail_address = None
        messagebox.showinfo("Success", "Address book updated successfully")
        self.tree.destroy()
        self.tree = self.add_table(AddressBook.load())

    def delete(self):
        if not self.detail_address:
            messagebox.showerror("Error", "Please select an item to delete")
            return
        if messagebox.askokcancel("Delete", "Do you want to delete?"):
            self.detail_address.delete()
            self.detail_window.destroy()
            self.detail_address = None
            messagebox.showinfo("Success", "Address book deleted successfully")
            self.tree.destroy()
            self.tree = self.add_table(AddressBook.load())

    def close_detail_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.detail_window.destroy()
            self.detail_address = None
        return


if __name__ == "__main__":
    gui = MyGUI()
