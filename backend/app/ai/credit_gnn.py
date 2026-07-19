import torch
import torch.nn.functional as F
from torch_geometric.nn import SAGEConv
from torch_geometric.data import Data
import torch_geometric.transforms as T

class CreditGNN(torch.nn.Module):
    def __init__(self, num_features: int = 8):
        super().__init__()
        self.conv1 = SAGEConv(num_features, 64)
        self.conv2 = SAGEConv(64, 32)
        self.fc1 = torch.nn.Linear(32, 16)
        self.fc2 = torch.nn.Linear(16, 1)
        self.dropout = torch.nn.Dropout(0.3)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = self.dropout(x)
        x = F.relu(self.conv2(x, edge_index))
        x = self.dropout(x)
        x = self.fc1(x.mean(dim=0))   # Graph-level pooling
        x = F.relu(x)
        x = self.fc2(x)
        return torch.sigmoid(x)

def build_mock_graph(features: dict):
    """Create mock graph from user features"""
    num_nodes = 5
    x = torch.rand(num_nodes, 8) * 0.6   # Base features
    
    # Inject real features
    if 'upi_velocity' in features:
        x[0, 0] = features['upi_velocity']
    if 'gst_filings' in features:
        x[0, 1] = features['gst_filings']
    
    # Edges: user connected to merchants
    edge_index = torch.tensor([
        [0, 0, 0, 0],   # User
        [1, 2, 3, 4]    # Merchants
    ], dtype=torch.long)
    
    data = Data(x=x, edge_index=edge_index)
    return T.NormalizeFeatures()(data)
