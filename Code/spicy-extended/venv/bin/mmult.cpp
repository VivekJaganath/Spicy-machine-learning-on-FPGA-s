#include "mmult.h"

#pragma SDS data access_pattern(a:SEQUENTIAL, b:SEQUENTIAL, c:SEQUENTIAL)
#pragma SDS data mem_attribute(a:PHYSICAL_CONTIGUOUS, b:PHYSICAL_CONTIGUOUS, c:PHYSICAL_CONTIGUOUS)
#pragma SDS data data_mover(a:AXIDMA_SIMPLE, b:AXIDMA_SIMPLE, c:AXIDMA_SIMPLE)
void mmult(int32_t a[1024],int32_t b[1024],int32_t c[1024],std::set<int> x) {

   int32_t A_tmp[1024];
   int32_t B_tmp[1024];
   std::set<string> c_tmp;
   c_tmp = {"hello", "world", "beautiful"};
   std::set<int> d_tmp;
   d_tmp = {1, 2, 3, 4};
   std::set<float> e_tmp;
   e_tmp = {1.252, 3.454, 4.7787};
#pragma HLS array_partition variable=A_tmp cyclic factor=16 dim=1
#pragma HLS array_partition variable=B_tmp block factor=16 dim=1

   for(int i=0; i<(int)32; i=i+1) {
      for(int j=0; j<(int)32; j=j+1) {
#pragma HLS PIPELINE
         A_tmp[(i)*32+j] = a[(i)*32+j];
         B_tmp[(i)*32+j] = b[(i)*32+j];
         c_tmp = x;
      }
   }
   for(int i=0; i<(int)32; i=i+1) {
      for(int j=0; j<(int)32; j=j+1) {
#pragma HLS PIPELINE
         int32_t result=0;
         for(int k=0; k<(int)32; k=k+1) {
            result+=(A_tmp[(i)*32+k]*B_tmp[(k)*32+j]);
         }
         c[(i)*32+j] = result;
      }
   }
}
