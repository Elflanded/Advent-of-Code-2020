package day13;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class DayThirteen {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("java/src/day13/DayThirteen.txt");
        Scanner scanner = new Scanner(file);
        List<String> inputs = new ArrayList<>();
        while (scanner.hasNextLine()) {
            inputs.add(scanner.nextLine());
        }

        partOne(inputs);
        partTwo(inputs);
    }

    public static void partOne(List<String> inputs) {
        int earlyTimestamp = Integer.parseInt(inputs.get(0));
        List<Integer> buses = new ArrayList<>();
        for (String s : inputs.get(1).split(",")) {
            if (s.equals("x")) continue;
            buses.add(Integer.parseInt(s));
        }

        int lowestTime = -1;
        int busId = 0;
        for (int bus : buses) {
            int timeDiff = bus - (earlyTimestamp % bus);
            if (lowestTime == -1 || lowestTime > timeDiff) {
                busId = bus;
                lowestTime = timeDiff;
            }
        }
        System.out.println(lowestTime * busId);
    }

    public static void partTwo(List<String> inputs) {
        List<String> inputList = Arrays.asList(inputs.get(1).split(","));

        long time = 100000000000000L;
        int index = 0;
        long add = 1;

        while (index < inputList.size()) {
            if (inputList.get(index).equals("x")) {
                index++;
                continue;
            }
            int value = Integer.parseInt(inputList.get(index));
            if ((time + index) % value == 0) {
                add *= value;
                index++;
                continue;
            }
            time += add;
        }

        System.out.println(time);
    }
}
