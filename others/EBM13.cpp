#include <iostream>
#include<math.h>
using namespace std;
int main()
{
	cout << endl;
	cout << "******************************************************************************************************" << endl;
	cout << "\t Exercise 1" << endl;
	cout << "Find the maximum allowable distance between the most distant stations of the local Ethernet network , if the values are known." << endl<<endl;
	float En_min, Vk= 10, Vc = 50000, Tp, Tn, Tc_max,Smax,Smax1;
	cout << "Data transfer rate over coaxial cable (transmission medium in the network)= " << Vk<< endl;
	cout << "signal propagation speed in the transmission medium= " << Vc << endl;
    cout << "minimum packet (frame) length = ";
    cin >> En_min;
    Tn = En_min / Vk;
	Tc_max = Tn/2;
	Smax = Vc * Tc_max;
	Smax1 = ((0.5*Vc)*(En_min/Vk));
	cout <<"The packet transmission time: " << Tc_max << endl;
	//cout << "Smax<= " << Smax<<endl;
	cout <<"The maximum allowable distance between the most distant stations of the local Ethernet network: " << Smax1 << endl;
	cout << endl;
	cout << "******************************************************************************************************" << endl;
	cout << "\t Exercise 2" << endl;
	cout << " " << endl<<endl;
	float Npc2 = 16, Vc2 = 50000, Te=500, Sk, Ek2 = 1024, Vk2,Tp_max2,Toj_max,Tobsl,Tob,Tc,Tk2,Toz;
	Vk2 = 10;
	cout << "Number of workstations in the network, Npc=  "<<Npc2 << endl;
	cout << "The speed of signal propagation through the coaxial cable (transmission medium), Vc= " <<Vc2<< endl;
	cout << "Delay time of a marker with a frame in one node (workstation) of the network, Te=  " << Te<< endl;
	cout << "Data transfer rate over a mono channel" <<Sk<< endl;
	cout << "Total marker and frame length, Ek= "<<Ek2 << endl;
	cout << "The length of the ring monochannel " ; cin >> Sk;
	Tc = (Sk / Vc2);
	Tk2 = (Ek2/ Vk2);
	Toz = Npc2 * Te;
	Tob = Tc + Tk2 + Toz;
	Tobsl = Tob;
	Toj_max = (Npc2 - 1) * Tob;
	Tp_max2 = Toj_max + Tobsl;
	cout << "The time during which the marker, together with the frame, makes a full revolution in the mono channel, Tob= "<<Tob << endl;
	cout << "The propagation time of the signal in the transmitting medium through the entire monochannel, Tc= "<<Tc << endl;
	cout << "The time of frame transmission through the entire mono-channel, Tk= " <<Tk2<< endl;
	cout << "The total delay time of the frame transmitted over the ring at the network nodes, Toz " <<Toz<< endl;
	cout << "The maximum waiting time for a request (frame) to be sent to a mono channel, Toj_max " <<Toj_max<< endl;
	cout << "Is the actual service time of the request, Tobsl= " <<Tobsl<< endl;
	cout << "Maximum response time to a user's request ( T p , max ) in a local network with a ring topology, Tp.max= " <<Tp_max2<< endl;
	cout << endl;
	cout << "******************************************************************************************************" << endl;
	cout << "\t Exercise 3" << endl;
	cout << "Determine the maximum time for transferring a frame from one workstation to another in a network with a star topology and handover of a token along a logical ring (a token moves sequentially from one PC to another in ascending order of their network numbers), if the following values are specified: " << endl << endl;
	float Spc3 = 0.6, Vc3=50000, Ek3=1024, Vk3 =10, T3=500, Npc3=16,Tmax,Tc3,Tk3;
	Vk3 =( 5 * pow(10, 6));
	cout << "\nThe distance between two PCs in the network (for all PCs it is assumed to be the same), Spc= " << Spc3<< endl;
	cout << "The speed of signal propagation in the transmission medium (in a coaxial cable)= "<<Vc3 << endl;
	cout << "Frame length together with a marker = "<<Ek3 << endl;
	cout << "Network data transfer rate = " <<Vk3<< endl;
	cout << "the number of workstations in the network = " <<Npc3<< endl;
    cout << "Frame delay time in one network node = "; cin >> T3;
	Tc3 = (Spc3 / Vc3) *( pow(10, 6));
	Tk3 = ((Ek3*8) / Vk3) * (pow(10, 6));
	Tmax = ((Tc3 + Tk3 + T3) * (Npc3 - 1));
	cout << "The propagation time of a signal in a transmission medium from one PC to another, Tc= " <<Tc3<< endl;
	cout << "The time   of frame transmission (together with the marker) from one PC to another, Tk= "<<Tk3 << endl;
	cout << "The maximum time to transfer a frame from one workstation ( PC ) of the network to another, Tmax= " <<Tmax<< endl;

	
	return 0;
}

