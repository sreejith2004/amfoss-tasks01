using System;
using System.Net;
using System.Net.Sockets;
using System.Text.RegularExpressions;

public class SynchronousSocketClient
{
    public static void StartClient()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];

        // Connect to a remote device.  
        try
        {
            // Establish the remote endpoint for the socket.  
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = ipHostInfo.AddressList[0];
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 8080);

            // Create a TCP/IP socket.  
            Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            // Connect the socket to the remote endpoint. Catch any errors.  
            try
            {
                sender.Connect(remoteEP);

                Console.WriteLine("Socket connected to {0}", sender.RemoteEndPoint.ToString());

                // Get person's data from the user
                string name = GetInput("Enter the Person Name: ", @"^[a-zA-Z]+$");
                string interests = GetInput("Enter the Person Interest: ", @"^[a-zA-Z\\s]+$");
                string mail = GetInput("Enter the Person Email: ", @"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

                // Encode the data string into a byte array.  
                byte[] msg = Encoding.ASCII.GetBytes(name + "," + interests + "," + mail);

                // Send the data through the socket.  
                int bytesSent = sender.Send(msg);

                Console.WriteLine("Data sent to server");

                // Close the socket.
                sender.Shutdown(SocketShutdown.Both);
                sender.Close();
            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
    }

    private static string GetInput(string message, string pattern)
    {
        Regex regex = new Regex(pattern);

        while (true)
        {
            Console.WriteLine(message);
            string input = Console.ReadLine();

            if (regex.IsMatch(input))
            {
                return input;
            }
            else
            {
                Console.WriteLine("Invalid input. Please try again.");
            }
        }
    }

    public static void Main(string[] args)
    {
        StartClient();
    }
}
