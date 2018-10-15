#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <time.h>
#include <cstdlib>

using namespace std;

/*
*/

void results2file(string filename, int argc, int j, double x[], double y[], double z[])
  {
    ofstream outfile("data/" + filename + to_string(j) + ".txt");
    if (!outfile.is_open())
      cout<<"Could not open file" << endl;
    else
    {
      for (int i = 0; i < argc; i++)
        outfile << setw(5) << x[i] << setw(5) << y[i] << setw(5) << z[i] << endl;
    }
  }

/*
*/

int main(int argc, char *argv[])
  {
  int n = atoi(argv[1]);
  int k = atoi(argv[2]);

  int seed = n;

  void srand(int seed);

  double *x = new double[n];
  double *y = new double[n];
  double *z = new double[n];

  for (int j = 0; j < k; j++)
  {
    x[0] = 0;
    y[0] = 0;
    z[0] = 0;

    for (int i = 0; i < n-1; i++)
      {
        x[i+1] = x[i] + rand() % 3 - 1;
        y[i+1] = y[i] + rand() % 3 - 1;
        z[i+1] = z[i] + rand() % 3 - 1;
      }
    results2file("data_", n, j, x, y, z);
  }

  delete [] x;
  delete [] y;
  delete [] z;

  return 0;
  }
