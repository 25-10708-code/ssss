import 'package:flutter/material.dart';

void main() {
  runApp(const MusicCommunityApp());
}

class MusicCommunityApp extends StatelessWidget {
  const MusicCommunityApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Music Mate',
      theme: ThemeData(
        brightness: Brightness.dark, // 음악 앱 특유의 힙한 다크 모드
        primaryColor: Colors.purpleAccent,
        scaffoldBackgroundColor: const Color(0xFF121212),
      ),
      home: const GenreSelectScreen(),
    );
  }
}

class GenreSelectScreen extends StatefulWidget {
  const GenreSelectScreen({super.key});

  @override
  State<GenreSelectScreen> createState() => _GenreSelectScreenState();
}

class _GenreSelectScreenState extends State<GenreSelectScreen> {
  // 제공할 음악 장르 리스트
  final List<String> _genres = ['인디 밴드', '힙합/랩', '시티팝', '재즈', 'K-POP', 'R&B', '클래식', '로파이(Lo-Fi)'];
  // 사용자가 선택한 장르를 담을 셋(Set)
  final Set<String> _selectedGenres = {};

  // 가상의 매칭 유저 데이터
  final List<Map<String, dynamic>> _dummyMates = [
    {'name': '음악덕후99', 'matchRate': '95%', 'genres': '시티팝, 로파이', 'song': 'Plastic Love'},
    {'name': '재즈가좋아', 'matchRate': '88%', 'genres': '재즈, R&B', 'song': 'Fly Me To The Moon'},
    {'name': '비트메이커', 'matchRate': '82%', 'genres': '힙합/랩, R&B', 'song': 'Bad Guy'},
  ];

  void _showMatchingDialog() {
    showModalBottomSheet(
      context: context,
      backgroundColor: const Color(0xFF1E1E1E),
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (context) {
        return Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                '🎵 당신과 취향이 통하는 메이트',
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
              ),
              const SizedBox(height: 15),
              ..._dummyMates.map((mate) => Card(
                color: const Color(0xFF2C2C2C),
                margin: const EdgeInsets.symmetric(vertical: 8),
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: Colors.purpleAccent,
                    child: Text(mate['matchRate']!, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.white)),
                  ),
                  title: Text(mate['name']!, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  subtitle: Text('선호: ${mate['genres']} \n지금 듣는 곡: ${mate['song']}', style: const TextStyle(color: Colors.grey, fontSize: 12)),
                  isThreeLine: true,
                  trailing: IconButton(
                    icon: const Icon(Icons.chat_bubble_outline, color: Colors.purpleAccent),
                    onPressed: () {
                      // 대화방 연결 등 추후 기능 확장
                    },
                  ),
                ),
              )),
            ],
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('🎧 Music Mate 찾기', style: TextStyle(fontWeight: FontWeight.bold)),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              '지금 끌리는 \n음악 장르를 골라보세요!',
              style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: Colors.white, height: 1.3),
            ),
            const SizedBox(height: 10),
            const Text('최소 1개 이상 선택하면 메이트를 찾을 수 있어요.', style: TextStyle(color: Colors.grey)),
            const SizedBox(height: 30),
            // 장르 선택 칩(Chip) 영역
            Expanded(
              child: Wrap(
                spacing: 10,
                runSpacing: 10,
                children: _genres.map((genre) {
                  final isSelected = _selectedGenres.contains(genre);
                  return ChoiceChip(
                    label: Text(genre),
                    selected: isSelected,
                    selectedColor: Colors.purpleAccent,
                    backgroundColor: const Color(0xFF2C2C2C),
                    labelStyle: TextStyle(
                      color: isSelected ? Colors.white : Colors.grey,
                      fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                    ),
                    onSelected: (selected) {
                      setState(() {
                        if (selected) {
                          _selectedGenres.add(genre);
                        } else {
                          _selectedGenres.remove(genre);
                        }
                      });
                    },
                  );
                }).toList(),
              ),
            ),
            // 매칭 시작 버튼
            SizedBox(
              width: double.infinity,
              height: 55,
              child: ElevatedButton(
                onPressed: _selectedGenres.isEmpty ? null : _showMatchingDialog,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.purpleAccent,
                  disabledBackgroundColor: Colors.grey[800],
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                ),
                child: Text(
                  _selectedGenres.isEmpty ? '장르를 선택해주세요' : '나와 닮은 음악 메이트 찾기',
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
