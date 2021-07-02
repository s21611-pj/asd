import java.io.*;

public class HuffmanDecoding {

    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader("src/file.txt"))) {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            while (line != null) {
                sb.append(line);
                sb.append(System.lineSeparator());
                line = br.readLine();
            }
            String everything = sb.toString();
            HuffmanAlgo huffAlg = new HuffmanAlgo();
            huffAlg.buildHuffmanTree(everything);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}