from mainEngine import mainEngine
import tkinter as tk

class frontend():
    def __init__(self) -> None:
        # self.url = url
        self.title = "YouTube Downloader"
        self.height = 500
        self.width = 800
        self.font = "Arial"

    def mainWindow(self):
        root = tk.Tk()

        root.title(self.title) #Title for the Window

        # window Height and Width
        self.windowSize(root)      

        heading = tk.Label(root,text="YouTube Downloader",font=(self.font,20)).pack(pady=25)
        
        # Root 1st Frame
        rootFrame = tk.Frame(root)
        rootFrame.pack()

        # Form Details
        self.formFrame(root,rootFrame)

        root.mainloop()

    def windowSize(self,root):
        root.minsize(self.width,self.height)
        root.maxsize(self.width,self.height)

    def formFrame(self,root,master):
        
        url_var = tk.StringVar()
        location_var = tk.StringVar()
        filetype_var = tk.StringVar(master,"Music")

        resultFrame = tk.Frame(root)
        
        
        url_label = tk.Label(master,text="URL",font=(self.font,12)).grid(row=0,column=0)
        url_entry = tk.Entry(master,textvariable=url_var,font=(self.font,15)).grid(row=0,column=1,padx=10,pady=10)


        location_lbl = tk.Label(master,text="Location",font=(self.font,12)).grid(row=1,column=0)
        location_entry = tk.Entry(master,textvariable=location_var,font=(self.font,15))
        location_entry.insert(tk.END,"Default")
        location_entry.grid(row=1,column=1,pady=10)

        filType_lbl = tk.Label(master,text="File Type",font=(self.font,12)).grid(row=2,column=0,pady=10)
 
        searchOption = tk.OptionMenu(master,filetype_var,"Music","Video","Playlist")
        searchOption.config(font=(self.font,12))
        searchOption.grid(row=2,column=1,sticky=tk.W,padx=5)
        
        submit_btn = tk.Button(master,text="Download",font=(self.font,12),borderwidth=3 ,command=lambda:self.DownloadFile(resultFrame,url_var.get(),location_var.get(),filetype_var.get())).grid(row=3,column=0,pady=12)

        reset_btn = tk.Button(master,text="Reset",font=(self.font,12),command=lambda:self.ResetCommand(resultFrame,url_var),borderwidth=3).grid(row=3,column=1,pady=12,padx=5,sticky=tk.W)

    def DownloadFile(self,master,url,location,fileType):
        mainEngine(url,location,fileType)
        master.pack()
        tk.Label(master,text=f"File Downloaded",fg="green",font=(self.font,18)).grid(row=4,column=1)
 
    def ResetCommand(self,master,url_var):
        try:
            url_var.set("")
            master.pack_forget()
        except Exception as e:
            print(e)

def main():
    frntend = frontend()
    frntend.mainWindow()

if __name__ == '__main__':
    main()
    