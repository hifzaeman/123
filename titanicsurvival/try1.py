import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer
import os

# Initialize pygame mixer
mixer.init()

# Player state variables
player_state = {
    'playlist': [],
    'current_track': 0,
    'is_playing': False,
    'is_paused': False,
    'now_playing_label': None,
    'playlist_box': None,
    'play_btn': None,
    'pause_btn': None,
    'volume_slider': None,
    'root': None
}

def add_songs():
    """Add songs to the playlist"""
    songs = filedialog.askopenfilenames(
        title="Select Music Files",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg"), ("All Files", "*.*")]
    )
    
    for song in songs:
        song_name = os.path.basename(song)
        player_state['playlist'].append(song)
        player_state['playlist_box'].insert(tk.END, song_name)

def remove_song():
    """Remove selected song from playlist"""
    try:
        selected_index = player_state['playlist_box'].curselection()[0]
        player_state['playlist_box'].delete(selected_index)
        player_state['playlist'].pop(selected_index)
        
        if selected_index == player_state['current_track'] and player_state['is_playing']:
            stop_music()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a song to remove")

def clear_playlist():
    """Clear all songs from playlist"""
    result = messagebox.askyesno("Clear Playlist", "Remove all songs from playlist?")
    if result:
        stop_music()
        player_state['playlist_box'].delete(0, tk.END)
        player_state['playlist'] = []
        player_state['current_track'] = 0
        player_state['now_playing_label'].config(text="No track selected")

def play_music():
    """Play the current track"""
    if not player_state['playlist']:
        messagebox.showinfo("Info", "Please add songs to the playlist first")
        return
    
    if player_state['is_paused']:
        mixer.music.unpause()
        player_state['is_paused'] = False
        player_state['is_playing'] = True
    else:
        try:
            mixer.music.load(player_state['playlist'][player_state['current_track']])
            mixer.music.play()
            player_state['is_playing'] = True
            player_state['is_paused'] = False
            
            song_name = os.path.basename(player_state['playlist'][player_state['current_track']])
            player_state['now_playing_label'].config(text=song_name)
            player_state['playlist_box'].selection_clear(0, tk.END)
            player_state['playlist_box'].selection_set(player_state['current_track'])
            player_state['playlist_box'].see(player_state['current_track'])
        except Exception as e:
            messagebox.showerror("Error", f"Could not play the song: {str(e)}")

def pause_music():
    """Pause the current track"""
    if player_state['is_playing'] and not player_state['is_paused']:
        mixer.music.pause()
        player_state['is_paused'] = True

def stop_music():
    """Stop the current track"""
    mixer.music.stop()
    player_state['is_playing'] = False
    player_state['is_paused'] = False

def next_track():
    """Play the next track in playlist"""
    if not player_state['playlist']:
        return
    
    player_state['current_track'] = (player_state['current_track'] + 1) % len(player_state['playlist'])
    stop_music()
    play_music()

def previous_track():
    """Play the previous track in playlist"""
    if not player_state['playlist']:
        return
    
    player_state['current_track'] = (player_state['current_track'] - 1) % len(player_state['playlist'])
    stop_music()
    play_music()

def play_selected(event):
    """Play the selected track from playlist"""
    try:
        selected_index = player_state['playlist_box'].curselection()[0]
        player_state['current_track'] = selected_index
        stop_music()
        play_music()
    except IndexError:
        pass

def change_volume(val):
    """Change the volume"""
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def create_widgets(root):
    """Create all UI widgets"""
    # Title bar
    title_frame = tk.Frame(root, bg="#16213e", height=60)
    title_frame.pack(fill=tk.X)
    
    title_label = tk.Label(
        title_frame,
        text="🎵 Music Player",
        font=("Arial", 20, "bold"),
        bg="#16213e",
        fg="#00d4ff"
    )
    title_label.pack(pady=15)
    
    # Now playing section
    now_playing_frame = tk.Frame(root, bg="#0f3460", height=80)
    now_playing_frame.pack(fill=tk.X, padx=20, pady=10)
    
    tk.Label(
        now_playing_frame,
        text="Now Playing:",
        font=("Arial", 11, "bold"),
        bg="#0f3460",
        fg="#00d4ff"
    ).pack(pady=(10, 5))
    
    player_state['now_playing_label'] = tk.Label(
        now_playing_frame,
        text="No track selected",
        font=("Arial", 13),
        bg="#0f3460",
        fg="white",
        wraplength=500
    )
    player_state['now_playing_label'].pack(pady=(0, 10))
    
    # Control buttons frame
    control_frame = tk.Frame(root, bg="#1a1a2e")
    control_frame.pack(pady=20)
    
    # Previous button
    prev_btn = tk.Button(
        control_frame,
        text="⏮️",
        font=("Arial", 20),
        command=previous_track,
        bg="#533483",
        fg="white",
        width=4,
        height=1,
        cursor="hand2",
        relief=tk.RAISED,
        bd=3
    )
    prev_btn.grid(row=0, column=0, padx=5)
    
    # Play button
    player_state['play_btn'] = tk.Button(
        control_frame,
        text="▶️",
        font=("Arial", 20),
        command=play_music,
        bg="#00d4ff",
        fg="white",
        width=4,
        height=1,
        cursor="hand2",
        relief=tk.RAISED,
        bd=3
    )
    player_state['play_btn'].grid(row=0, column=1, padx=5)
    
    # Pause button
    player_state['pause_btn'] = tk.Button(
        control_frame,
        text="⏸️",
        font=("Arial", 20),
        command=pause_music,
        bg="#e94560",
        fg="white",
        width=4,
        height=1,
        cursor="hand2",
        relief=tk.RAISED,
        bd=3
    )
    player_state['pause_btn'].grid(row=0, column=2, padx=5)
    
    # Stop button
    stop_btn = tk.Button(
        control_frame,
        text="⏹️",
        font=("Arial", 20),
        command=stop_music,
        bg="#c23b22",
        fg="white",
        width=4,
        height=1,
        cursor="hand2",
        relief=tk.RAISED,
        bd=3
    )
    stop_btn.grid(row=0, column=3, padx=5)
    
    # Next button
    next_btn = tk.Button(
        control_frame,
        text="⏭️",
        font=("Arial", 20),
        command=next_track,
        bg="#533483",
        fg="white",
        width=4,
        height=1,
        cursor="hand2",
        relief=tk.RAISED,
        bd=3
    )
    next_btn.grid(row=0, column=4, padx=5)
    
    # Volume control
    volume_frame = tk.Frame(root, bg="#1a1a2e")
    volume_frame.pack(pady=10)
    
    tk.Label(
        volume_frame,
        text="🔊 Volume:",
        font=("Arial", 11, "bold"),
        bg="#1a1a2e",
        fg="white"
    ).pack(side=tk.LEFT, padx=10)
    
    player_state['volume_slider'] = tk.Scale(
        volume_frame,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        command=change_volume,
        bg="#0f3460",
        fg="white",
        highlightthickness=0,
        length=300,
        cursor="hand2"
    )
    player_state['volume_slider'].set(70)
    player_state['volume_slider'].pack(side=tk.LEFT)
    
    # Playlist section
    playlist_label = tk.Label(
        root,
        text="📃 Playlist",
        font=("Arial", 14, "bold"),
        bg="#1a1a2e",
        fg="#00d4ff"
    )
    playlist_label.pack(pady=(20, 5))
    
    # Playlist listbox with scrollbar
    list_frame = tk.Frame(root, bg="#1a1a2e")
    list_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
    
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    player_state['playlist_box'] = tk.Listbox(
        list_frame,
        font=("Arial", 11),
        bg="#0f3460",
        fg="white",
        selectmode=tk.SINGLE,
        yscrollcommand=scrollbar.set,
        selectbackground="#00d4ff",
        selectforeground="black",
        cursor="hand2"
    )
    player_state['playlist_box'].pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=player_state['playlist_box'].yview)
    
    player_state['playlist_box'].bind("<Double-Button-1>", play_selected)
    
    # Playlist control buttons
    playlist_btn_frame = tk.Frame(root, bg="#1a1a2e")
    playlist_btn_frame.pack(pady=10)
    
    add_btn = tk.Button(
        playlist_btn_frame,
        text="➕ Add Songs",
        font=("Arial", 11, "bold"),
        command=add_songs,
        bg="#27ae60",
        fg="white",
        cursor="hand2",
        padx=15,
        pady=8
    )
    add_btn.pack(side=tk.LEFT, padx=5)
    
    remove_btn = tk.Button(
        playlist_btn_frame,
        text="➖ Remove Song",
        font=("Arial", 11, "bold"),
        command=remove_song,
        bg="#e74c3c",
        fg="white",
        cursor="hand2",
        padx=15,
        pady=8
    )
    remove_btn.pack(side=tk.LEFT, padx=5)
    
    clear_btn = tk.Button(
        playlist_btn_frame,
        text="🗑️ Clear Playlist",
        font=("Arial", 11, "bold"),
        command=clear_playlist,
        bg="#c0392b",
        fg="white",
        cursor="hand2",
        padx=15,
        pady=8
    )
    clear_btn.pack(side=tk.LEFT, padx=5)

def main():
    """Main function to run the music player"""
    root = tk.Tk()
    root.title("Music Player 🎵")
    root.geometry("600x600")
    root.configure(bg="#1a1a2e")
    
    player_state['root'] = root
    create_widgets(root)
    
    root.mainloop()

# Run the app
if __name__ == "__main__":
    main()