using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class SynchronousSocketListener
{
    // Incoming data from the client.  
    public static string data = null;

    public static void StartListening()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];

        // Establish the local endpoint for the socket.  
        // Dns.GetHostName returns the name of the
        // host running the application.  
        IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
        IPAddress ipAddress = ipHostInfo.AddressList[0];
        IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 8080);

        // Check whether TCP Socket is created correctly
        Socket listener = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

        // Bind the socket to the local endpoint and
        // listen for incoming connections.  
        string fileName = "file.json";
        try
        {
            listener.Bind(localEndPoint);
            listener.Listen(10);

            // Start listening for connections.  
            while (true)
            {
                Console.WriteLine("Waiting for a connection...");
                // Program is suspended while waiting for an incoming connection.  
                Socket handler = listener.Accept();
                data = null;

                // An incoming connection needs to be processed.  
                // check if the variable is defined or not also even correctly defined
                int bytesRec = handler.Receive(bytes);
                data = Encoding.ASCII.GetString(bytes, 0, bytesRec);
                //Console.WriteLine("Text received : {0}", data);
                string[] dataArr = data.Split(',');
                string name = dataArr[0];
                string interests = dataArr[1];
                string mail = dataArr[2];
                string jsonData = "{ \"name\": \"" + name + "\", \"interests\": \"" + interests + "\", \"email\": \"" + mail + "\" }";
                Console.WriteLine("Name: {0}", name);
                Console.WriteLine("Interests: {0}", interests);
                Console.WriteLine("Email: {0}", mail);
                if (File.Exists(fileName))
                {
                    using (StreamWriter sw = File.AppendText(fileName))
                    {
                        sw.WriteLine(jsonData);
                    }
                }
                else
                {
                    using (StreamWriter sw = File.CreateText(fileName))
                    {
                        sw.WriteLine(jsonData);
                    }
                }
                handler.Shutdown(SocketShutdown.Both);
                handler.Close();
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }

        Console.WriteLine("\nPress ENTER to continue...");
        Console.Read();
    }

    // check the main function
    public static void Main(string[] args)
    {
        StartListening();
    }
}
