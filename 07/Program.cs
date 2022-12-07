Dictionary<string, int> fileStructure = new Dictionary<string, int>();
int totalSum = 0;
// Read and traverse the file
using (StreamReader sr = new StreamReader(@".\input.txt")) 
{
    while (sr.Peek() >= 0)
    {
        readDirectory(sr, "root");
    }
}

// Recursive funtion that goes through the lines: summate the quanties and the returns
(string, int) readDirectory(StreamReader sr, string directoryName){
    string line = "";
    int quantity = 0;
    int val = 0;
    bool isWalking = true;
    while(isWalking){
        if(sr.EndOfStream)
        {
            return (directoryName,quantity);
        }
        line = sr.ReadLine().Replace("$ ","");
        if(line.Equals("cd ..")){
            isWalking = false;
            break;
        }
        if(int.TryParse(line.Split(' ')[0],out val)){
            quantity += val;
        }
        else{
            switch (line.Split(' ')[0])
            {
                case "dir":
                    break;
                case "cd ..":
                    isWalking = false;
                    break; //return
                case "ls":
                    break; //Read next line
                default: //cd Directory
                    var s = readDirectory(sr,string.Concat(directoryName,'/',line.Split(' ')[1]));
                    fileStructure.Add(s.Item1,s.Item2);
                    quantity += s.Item2;
                    break; //Go into next directory (recursive call)
            }
        }
    }
    return (directoryName,quantity);   
}




// **** PART 1 START ***** //
foreach(KeyValuePair<string, int> entry in fileStructure){
    if(entry.Value < 100000)
        totalSum +=entry.Value;
}
System.Console.WriteLine($"Answer Part 1: {totalSum.ToString()}");
// **** PART 1 END ***** //

// **** PART 2 START ***** //
int totalSpace = 70000000;
int requiredSpace = 30000000;

int lowestFolder = fileStructure["root//"];
int remainingSpace = totalSpace - lowestFolder;
foreach(KeyValuePair<string, int> entry in fileStructure){
    if(remainingSpace + entry.Value >= requiredSpace)
    {
        if(entry.Value < lowestFolder)
        {
            lowestFolder = entry.Value;
        }
    }
}
// **** PART 2 END ***** //
System.Console.WriteLine($"Answer Part 2: {lowestFolder.ToString()}")
System.Console.ReadKey();  